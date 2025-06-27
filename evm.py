from eth_account import Account
from mnemonic import Mnemonic
import json
from pathlib import Path

# Bật tính năng tạo ví từ mnemonic
Account.enable_unaudited_hdwallet_features()

# Tạo cụm từ ghi nhớ (mnemonic)
mnemo = Mnemonic("english")
mnemonic_phrase = mnemo.generate(strength=128)

# Tạo ví từ mnemonic
acct = Account.from_mnemonic(mnemonic_phrase)

# Lấy private key và địa chỉ ví
private_key = acct.key.hex()
wallet_address = acct.address

# Hiển thị địa chỉ ví
print("🎉 Địa chỉ ví EVM của bạn là:", wallet_address)

# Ghi thông tin vào file
data = {
    "mnemonic": mnemonic_phrase,
    "private_key": private_key
}
with open("wallet_info.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("📁 Đã lưu vào file wallet_info.json")
