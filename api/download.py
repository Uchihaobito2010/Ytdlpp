import json
import subprocess

# ==========================================
#  API Developed by Paras
#  Brand      : TOBI / OBITO
#  Website    : https://Aotpy.vercel.app
#  Contact    : @Aotpy
# ==========================================

def handler(request):
    try:
        body = json.loads(request.body or "{}")
        url = body.get("url")

        if not url:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({
                    "success": False,
                    "error": "URL is required",
                    "credits": {
                        "developer": "Paras",
                        "brand": "Tobi / Obito",
                        "website": "https://Aotpy.vercel.app",
                        "contact": "@Aotpy"
                    }
                })
            }

        cmd = ["yt-dlp", "-f", "best", "-g", url]
        direct_url = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT
        ).decode().strip()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": True,
                "download_url": direct_url,
                "credits": {
                    "developer": "Paras",
                    "brand": "Tobi / Obito",
                    "website": "https://Aotpy.vercel.app",
                    "contact": "@Aotpy"
                }
            })
        }

    except subprocess.CalledProcessError as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": False,
                "error": "Failed to fetch media",
                "details": e.output.decode(),
                "credits": {
                    "developer": "Paras",
                    "brand": "Tobi / Obito",
                    "website": "https://Aotpy.vercel.app",
                    "contact": "@Aotpy"
                }
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": False,
                "error": str(e),
                "credits": {
                    "developer": "Paras",
                    "brand": "Tobi / Obito",
                    "website": "https://Aotpy.vercel.app",
                    "contact": "@Aotpy"
                }
            })
        }
