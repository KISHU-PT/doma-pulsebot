# doma_utils.py

def generate_doma_link(domain_name: str) -> str:
    """Return full link to the domain on Doma testnet"""
    return f"https://start.doma.xyz/market/{domain_name}"


def format_event_message(domain: str, price: float) -> str:
    """Return a styled alert message for Telegram"""
    link = generate_doma_link(domain)
    return (
        f"🔥 *New Domain Sale!*\n"
        f"🌐 Domain: `{domain}`\n"
        f"💰 Price: *{price:.2f} USDC*\n"
        f"🔗 [View on Doma]({link})"
    )


def get_tld(domain: str) -> str:
    """Extract the TLD from a domain name (e.g., '.ape')"""
    if "." in domain:
        return "." + domain.split(".")[-1]
    return ""


def contains_keyword(domain: str, keyword: str) -> bool:
    """Check if a keyword exists in domain name (case-insensitive)"""
    return keyword.lower() in domain.lower()
