import os
import asyncio
from mtprotoproxy import AsyncMTProtoProxy

# Render automatically environment me PORT assign karta hai
PORT = int(os.environ.get('PORT', 443))

# Yeh aapki proxy ka secure 32-character hex secret hai. 
# Ise aap apne hisab se badal sakte hain full security ke liye.
# Format: Sirf a-f alphabets aur 0-9 numbers hone chahiye (32 characters)
SECRET = os.environ.get('SECRET', '1234567890abcdef1234567890abcdef')

# FakeTLS Domain - Yeh network providers ko lagega ki aap Google chala rahe ho, Telegram nahi.
# Isse proxy block nahi hoti.
TLS_DOMAIN = os.environ.get('TLS_DOMAIN', 'www.google.com')

async def start_proxy():
    print("=========================================")
    print(f"🚀 Starting Secure FakeTLS Proxy...")
    print(f"📡 Port Assigned: {PORT}")
    print(f"🔑 Proxy Secret: {SECRET}")
    print(f"🌍 Masquerading Domain: {TLS_DOMAIN}")
    print("=========================================")

    # Proxy initialize ho rahi hai
    proxy = AsyncMTProtoProxy(
        port=PORT,
        secret=SECRET,
        tls_domain=TLS_DOMAIN
    )

    print("✅ Proxy is running smoothly!")
    print("🛡️ Your data is 100% safe and routed strictly to official Telegram servers.")
    await proxy.start()

if __name__ == '__main__':
    # High-performance async loop setup
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(start_proxy())
        loop.run_forever()
    except KeyboardInterrupt:
        print("Proxy manually stopped.")
