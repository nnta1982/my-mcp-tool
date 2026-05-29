from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-simple-tool")

@mcp.tool()
def cong_hai_so(a: float, b: float) -> float:
    """Cộng 2 số lại với nhau"""
    return a + b

@mcp.tool()
def nhan_hai_so(a: float, b: float) -> float:
    """Nhân 2 số lại với nhau"""
    return a * b