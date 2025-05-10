from fastapi import FastAPI
import asyncio
import json
import sys
import logging
from typing import Any, Callable, Dict, List, Optional, Union

class FastMCP:
    """A simple FastMCP implementation for the Archon project."""
    
    def __init__(self, name: str = "fastmcp", log_level: str = "INFO"):
        """Initialize the FastMCP server.
        
        Args:
            name: The name of the MCP server
            log_level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.name = name
        self.app = FastAPI(title=f"{name} MCP Server")
        self.tools = {}
        
        # Set up logging
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError(f"Invalid log level: {log_level}")
        
        logging.basicConfig(
            level=numeric_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(name)
    
    def tool(self, name: str = None):
        """Decorator to register a function as a tool."""
        def decorator(func):
            nonlocal name
            tool_name = name or func.__name__
            self.tools[tool_name] = func
            return func
        return decorator
    
    async def handle_request(self, request_data):
        """Handle an incoming request."""
        try:
            request = json.loads(request_data)
            tool_name = request.get("name")
            params = request.get("parameters", {})
            
            if tool_name not in self.tools:
                return {"error": f"Tool '{tool_name}' not found"}
            
            tool_func = self.tools[tool_name]
            result = await tool_func(**params)
            
            return {"result": result}
        except Exception as e:
            self.logger.error(f"Error processing request: {str(e)}")
            return {"error": str(e)}
    
    def run(self, transport: str = "stdio", host: str = "0.0.0.0", port: int = 3100):
        """Run the MCP server.
        
        Args:
            transport: The transport method ('stdio' or 'http')
            host: The host to bind to for HTTP transport
            port: The port to bind to for HTTP transport
        """
        if transport == "stdio":
            self.logger.info(f"Starting {self.name} MCP server with stdio transport")
            asyncio.run(self._run_stdio())
        elif transport == "http":
            import uvicorn
            self.logger.info(f"Starting {self.name} MCP server with HTTP transport on {host}:{port}")
            uvicorn.run(self.app, host=host, port=port)
        else:
            raise ValueError(f"Invalid transport method: {transport}")
    
    async def _run_stdio(self):
        """Run the server using stdio transport."""
        self.logger.info("Listening for requests on stdin")
        while True:
            try:
                # Read a line from stdin
                line = sys.stdin.readline().strip()
                if not line:
                    continue
                
                # Process the request
                response = await self.handle_request(line)
                
                # Write the response to stdout
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
            except Exception as e:
                self.logger.error(f"Error in stdio transport: {str(e)}")
                # Try to recover and continue
                continue
