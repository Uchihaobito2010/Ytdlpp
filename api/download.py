import json
import subprocess
import tempfile
import os

def handler(request):
    try:
        body = json.loads(request.body)
        url = body.get("url")

        if not url:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "success": False,
                    "error": "URL is required"
                })
            }

        # temp file
        with tempfile.NamedTemporaryFile(delete=False) as f:
            output = f.name

        cmd = [
            "yt-dlp",
            "-f", "best",
            "-g",
            url
        ]

        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "success": True,
                "download_url": result
            })
        }

    except subprocess.CalledProcessError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": e.output.decode()
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "error": str(e)
            })
        }
