def create_user(name, surname, email, *, age, is_active=True):
    """
    Kullanıcı oluşturma fonksiyonu.
    'name', 'surname', 'email' pozisyonel veya anahtar kelime ile verilebilir.
    '*' işaretinden sonra gelen 'age' ve 'is_active' SADECE anahtar kelime ile verilmelidir.
    'is_active' için varsayılan değer True'dur.
    """
    print(f"Kullanıcı Oluşturuldu:")
    print(f"  Ad: {name}")
    print(f"  Soyad: {surname}")
    print(f"  Email: {email}")
    print(f"  Yaş: {age}")
    print(f"  Aktif: {is_active}")
    print("-" * 30)

print("--- Doğru Kullanım Örnekleri ---")

# 1. Tüm argümanları anahtar kelime ile sağlamak (her zaman geçerlidir)
# Keyword-only argümanlar (age, is_active) burada zorunlu olarak anahtar kelime ile veriliyor.
create_user(name="Ali", surname="Veli", email="ali.veli@example.com", age=30, is_active=True)

# 2. Pozisyonel argümanları pozisyonel, keyword-only argümanları anahtar kelime ile sağlamak
# '*' işaretinden sonra gelen 'age' ve 'is_active' sadece anahtar kelime olarak kullanılabilir.
create_user("Ayşe", "Yılmaz", "ayse.yilmaz@example.com", age=25) # is_active varsayılan değeri kullanır

print("\n--- Hatalı Kullanım Örnekleri (Beklenen Hatalar) ---")

# 3. Hata: Keyword-only argümanı pozisyonel olarak geçirmeye çalışmak
# 'age' argümanı '*' işaretinden sonra tanımlandığı için sadece anahtar kelime olarak geçirilmelidir.
try:
    create_user("Mehmet", "Demir", "mehmet.demir@example.com", 40, True)
except TypeError as e:
    print(f"Hata yakalandı (TypeError): {e}")
    print("Açıklama: 'age' ve 'is_active' keyword-only argümanlardır ve pozisyonel olarak verilemez.")
    print("-" * 30)

# 4. Hata: Gerekli bir keyword-only argümanı (age) atlamak
# 'age' için varsayılan değer tanımlanmadığı için zorunludur.
try:
    create_user("Zeynep", "Can", "zeynep.can@example.com")
except TypeError as e:
    print(f"Hata yakalandı (TypeError): {e}")
    print("Açıklama: 'age' zorunlu bir keyword-only argümandır ve sağlanmalıdır.")
    print("-" * 30)

# 5. Hata: Gerekli bir keyword-only argümanı (age) atlamak, diğerlerini pozisyonel vermek
try:
    create_user("Can", "Kara", "can.kara@example.com", is_active=False)
except TypeError as e:
    print(f"Hata yakalandı (TypeError): {e}")
    print("Açıklama: 'age' zorunlu bir keyword-only argümandır ve sağlanmalıdır.")
    print("-" * 30)

print("\n--- Fonksiyon tanımında '*' kullanımı ---")
print("def create_user(name, surname, email, *, age, is_active=True):")
print("  Yukarıdaki tanımda, '*' işaretinden önceki argümanlar (name, surname, email) pozisyonel veya anahtar kelime ile verilebilir.")
print("  '*' işaretinden sonraki argümanlar (age, is_active) SADECE anahtar kelime ile verilmelidir.")
print("  Bu, fonksiyon çağrılarının okunabilirliğini artırır ve argümanların amacını netleştirir.")