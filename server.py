from mcp.server.fastmcp import FastMCP
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

# Khởi tạo MCP
mcp = FastMCP("my-simple-tool")

@mcp.tool()
def cong_hai_so(a: float, b: float) -> float:
    """Cộng 2 số lại với nhau"""
    return a + b

@mcp.tool()
def nhan_hai_so(a: float, b: float) -> float:
    """Nhân 2 số lại với nhau"""
    return a * b


# ====================== CONFIG CHO DOCKER + RAILWAY ======================
app = mcp.streamable_http_app()   # Hoặc mcp.http_app() tùy version

# Fix lỗi Invalid Host Header
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*", ".up.railway.app", ".railway.app", "localhost"]
)

# CORS (rất cần khi dùng remote)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chạy trực tiếp bằng uvicorn (khuyến nghị khi dùng Docker)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=False
    )