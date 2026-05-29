import streamlit.components.v1 as components

def render():
    """Injects a client-side JavaScript timer that won't block the Python thread."""
    
    # HTML/JS payload for a dark-themed, mobile-friendly timer
    timer_html = """
    <div style="font-family: system-ui, -apple-system, sans-serif; color: white; text-align: center; padding: 10px; background: #262730; border-radius: 10px; border: 1px solid #444;">
        <div id="display" style="font-size: 32px; font-weight: bold; margin-bottom: 12px; font-variant-numeric: tabular-nums;">
            ⏱️ 00:00
        </div>
        <div style="display: flex; gap: 10px; justify-content: center;">
            <button onclick="startTimer(180)" style="flex: 1; padding: 12px; background: #FF4B4B; color: white; border: none; border-radius: 6px; font-size: 14px; font-weight: bold; cursor: pointer;">
                3 Min (Heavy)
            </button>
            <button onclick="startTimer(90)" style="flex: 1; padding: 12px; background: #31333F; color: white; border: 1px solid #666; border-radius: 6px; font-size: 14px; font-weight: bold; cursor: pointer;">
                90s (Accessory)
            </button>
        </div>
    </div>

    <script>
        let countdown;
        function startTimer(seconds) {
            clearInterval(countdown);
            const display = document.getElementById('display');
            const now = Date.now();
            const then = now + seconds * 1000;

            display.innerHTML = '⏱️ ' + formatTime(seconds);

            countdown = setInterval(() => {
                const secondsLeft = Math.round((then - Date.now()) / 1000);
                
                if (secondsLeft <= 0) {
                    clearInterval(countdown);
                    display.innerHTML = "💥 TIME TO LIFT!";
                    // Trigger iPhone haptic vibration (pattern: buzz, pause, buzz, pause, long buzz)
                    if (navigator.vibrate) {
                        window.navigator.vibrate([200, 100, 200, 100, 500]);
                    }
                    return;
                }
                display.innerHTML = '⏱️ ' + formatTime(secondsLeft);
            }, 1000);
        }

        function formatTime(secs) {
            const m = Math.floor(secs / 60);
            const s = secs % 60;
            return m + ':' + (s < 10 ? '0' : '') + s;
        }
    </script>
    """
    
    # Render the HTML block with a fixed height to prevent mobile layout shifting
    components.html(timer_html, height=130)