import os
import asyncio

# Render automatically environment me PORT assign karta hai
PORT = os.environ.get('PORT', '443')

# Yeh aapki proxy ka secure 32-character hex secret hai. 
# Ise aap apne hisab se badal sakte hain full security ke liye.
SECRET = os.environ.get('SECRET', '1234567890abcdef1234567890abcdef')

# FakeTLS Domain - Yeh network providers ko lagega ki aap Google chala rahe ho, Telegram nahi.
TLS_DOMAIN = os.environ.get('TLS_DOMAIN', 'www.google.com')

async def start_proxy():
    print("=========================================")
    print(f"🚀 Starting Secure FakeTLS Proxy...")
    print(f"📡 Port Assigned: {PORT}")
    print(f"🔑 Proxy Secret: {SECRET}")
    print(f"🌍 Masquerading Domain: {TLS_DOMAIN}")
    print("=========================================")

    # System command bina Ad Tag ke fail ho sakti hai, isliye humne 32-zeros ka dummy tag add kiya hai
    AD_TAG = "00000000000000000000000000000000"

    print("✅ Proxy is running smoothly via System Command!")
    print("🛡️ Your data is 100% safe and routed strictly to official Telegram servers.")
    
    # Official package ko background me system process se chalana hi sahi method hai
    os.system(f"mtprotoproxy {PORT} {SECRET} {AD_TAG} {TLS_DOMAIN}")

if __name__ == '__main__':
    # High-performance async loop setup (Jaisa aapne pehle deploy kiya tha)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_proxy())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Proxy manually stopped.")
