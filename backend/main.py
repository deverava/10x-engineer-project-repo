"""PromptLab API Server

Run with: python main.py
"""

# import uvicorn
# from app.api import app

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
"""PromptLab API Server

Run with: python main.py
"""

# import uvicorn

# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)

import uvicorn
from app.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
