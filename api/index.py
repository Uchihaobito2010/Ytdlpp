import json
import subprocess

# ================================
#  Developed by Paras
#  Brand   : TOBI / OBITO
#  Web     : https://Aotpy.vercel.app
#  Contact : @Aotpy
# ================================

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
                    "error": "url is required",
                    "credits": "Paras | Tobi / Obito | @Aotpy"
                })
            }

        cmd = ["yt-dlp", "-f", "best", "-g", url]
        media_url = subprocess.check_output(
            cmd, stderr=subprocess.STDOUT
        ).decode().strip()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": True,
                "download_url": media_url,
                "credits": "Paras | Tobi / Obito | @Aotpy"
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "success": False,
                "error": str(e),
                "credits": "Paras | Tobi / Obito | @Aotpy"
            })
        }
