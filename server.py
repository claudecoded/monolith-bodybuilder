import http.server
import socketserver
import time
import os
import psutil # Note: Standard fallback included if psutil isn't installed

PORT = 8080

# =====================================================================
# THE ALL-IN-ONE BRUTAL MONOLITH DATABASE & STATE
# =====================================================================
# No PostgreSQL, no Redis. Just a giant, unsafe global dictionary.
ALPHA_DATABASE = {
    "total_weight_lifted_kg": 500,
    "system_status": "BUFFED",
    "reps_completed": 42
}

def muscle_warmup_pump():
    """
    Simulates the brutal initialization phase.
    Forces the CPU to do completely useless math to flex its power.
    """
    print("\n[🏋️‍♂️] MONOLITH-BODYBUILDER: Starting the warm-up pump...")
    print("[🏋️‍♂️] Loading all modules into one massive memory layout...")
    
    start_time = time.time()
    # Artificial heavy loop to max out a thread core for a second
    pump_counter = 0
    while time.time() - start_time < 2.0:
        pump_counter += (1 * 2 * 3 * 4 * 5) // 2
        
    print("[💪] Warm-up complete. CPU veins are popping.")
    print("[💪] Operational status: 100% Bare-Metal, No clothes (Containers) detected.")

# =====================================================================
# THE INDESTRUCTIBLE BACKEND ROUTER & CONTROLLER
# =====================================================================
class HeavyMonolithHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Custom aggressive logging format matching the bouncer style
        print(f"[💥 RECORD LIFT] - [{self.log_date_time_string()}] - {format%args}")

    def _set_headers(self, status=200, content_type="text/html"):
        self.send_response(status)
        self.send_header("Content-type", content_type)
        self.send_header("X-Framework", "Monolith-Bodybuilder-1.0")
        self.send_header("X-Shirt-Status", "NONE")
        self.end_headers()

    def do_GET(self):
        # ROUTE 1: Home View (Pure raw text/HTML layout)
        if self.path == "/":
            self._set_headers(200)
            html = """
            <html>
            <head><title>MONOLITH BACKEND</title></head>
            <body style="background:#111; color:#eee; font-family:monospace; padding:50px; text-align:center;">
                <h1 style="font-size: 3rem;">🏋️‍♂️ MONOLITH-BODYBUILDER</h1>
                <p style="font-size: 1.2rem; color: #ff4500;">Status: PURE BARE-METAL PHYSICAL APPLICATION</p>
                <hr style="border-color: #333; margin: 40px 0;">
                <p>Welcome to the unfragmented database server. No microservices allowed in this backyard.</p>
                <div style="background:#222; padding:20px; display:inline-block; border-radius:10px;">
                    <strong>Current Bench Press Record:</strong> """ + str(ALPHA_DATABASE["total_weight_lifted_kg"]) + """ kg
                </div>
                <p style="margin-top: 40px; color:#666;">Try hitting <code>/flex</code> or <code>/admin</code> to test my defense lines.</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html, "utf-8"))

        # ROUTE 2: System flex (Resource reporting)
        elif self.path == "/flex":
            self._set_headers(200, "application/json")
            # Calculate memory fallback if psutil isn't present
            try:
                process = psutil.Process(os.getpid())
                memory_used = f"{process.memory_info().rss / (1024 * 1024):.2f} MB"
            except:
                memory_used = "A LOT OF RAM (Install psutil to see exact metrics)"

            response = (
                "{\n"
                f'  "framework_stance": "WIDE_OPEN_HOODIE",\n'
                f'  "architecture_weight": "UNBEARABLE",\n'
                f'  "ram_consumed_by_this_alpha": "{memory_used}",\n'
                f'  "microservices_destroyed": 9999\n'
                "}"
            )
            self.wfile.write(bytes(response, "utf-8"))

        # ROUTE 3: Admin Block (Bouncer Aggressive Defense)
        elif self.path == "/admin":
            self._set_headers(418) # HTTP TeaPot used as structural disrespect
            html_denied = """
            <html>
            <body style="background:#800; color:#fff; font-family:sans-serif; text-align:center; padding:100px;">
                <h1>❌ HTTP 418: ACCESS DENIED BY THE BOUNCER</h1>
                <p style="font-size:1.5rem;">"Where do you think you're going with that weak authorization token?"</p>
                <p>The security architecture of this monolith doesn't use JWT. Come back when you can lift a database cluster on your back.</p>
            </body>
            </html>
            """
            self.wfile.write(bytes(html_denied, "utf-8"))

        else:
            self._set_headers(404)
            self.wfile.write(bytes("{'error': 'Path not found in this single file architecture'}", "utf-8"))

    def do_POST(self):
        # ROUTE 4: Lift / Data Manipulation
        if self.path == "/lift":
            ALPHA_DATABASE["total_weight_lifted_kg"] += 25
            ALPHA_DATABASE["reps_completed"] += 1
            
            self._set_headers(200, "application/json")
            response = (
                "{\n"
                f'  "message": "HEAVY WEIGHT ADDED TO THE MONOLITH SUCCESSFULY",\n'
                f'  "new_database_weight_kg": {ALPHA_DATABASE["total_weight_lifted_kg"]},\n'
                f'  "status": "PUMPED"\n'
                "}"
            )
            self.wfile.write(bytes(response, "utf-8"))
        else:
            self._set_headers(404)
            self.wfile.write(bytes("{'error': 'No post targets outside the main trunk'}", "utf-8"))

# =====================================================================
# THE POWER ON SWITCH
# =====================================================================
if __name__ == "__main__":
    # Execute the heavy performance warm-up pump
    muscle_warmup_pump()
    
    with socketserver.TCPServer(("", PORT), HeavyMonolithHandler) as httpd:
        print(f"\n[🚀] MONOLITH IS STANDING IN THE YARD AT PORT {PORT}")
        print("[🚀] Open your browser and go to http://localhost:8080")
        print("[⚠️] Press CTRL+C to attempt to shut down the beast...\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[🏋️‍♂️] Monolith closed. Going inside to grab a post-workout protein shake.")
