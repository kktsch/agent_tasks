from decimal import Decimal, getcontext
from typing import Optional

class Calculator:
    """
    Matematiksel işlemler için güvenli hesap makinesi sınıfı.
    Hassas hesaplamalar için Decimal kullanır.
    """
    
    def __init__(self, precision: int = 10):
        """
        Hesap makinesini belirtilen hassasiyetle başlatır.
        
        Parametreler:
            precision (int): Hesaplamalar için ondalık basamak sayısı (varsayılan: 10)
        """
        self.precision = precision
        getcontext().prec = precision

    def evaluate(self, expression: str) -> Optional[Decimal]:
        """
        Matematiksel ifadeyi güvenli bir şekilde değerlendirir.
        
        Parametreler:
            expression (str): Değerlendirilecek matematiksel ifade (+, -, *, /, ^, parantez destekler)
        
        Dönüş Değeri:
            Optional[Decimal]: Hesaplama sonucu veya hata durumunda None
            
        Örnekler:
            >>> calc = Calculator()
            >>> calc.evaluate("2 + 2")     # Basit toplama
            >>> calc.evaluate("2 ^ 3")     # Üs alma işlemi
            >>> calc.evaluate("(4 + 5)/3") # Parantez ve bölme işlemi
        """
        try:
            cleaned_expr = self._sanitize_expression(expression)
            if not self._is_safe_expression(cleaned_expr):
                raise ValueError("Geçersiz veya güvenli olmayan ifade")
            
            if '^' in cleaned_expr:
                cleaned_expr = cleaned_expr.replace('^', '**')
                
            result = eval(cleaned_expr, {"__builtins__": None}, self._safe_functions())
            return Decimal(str(result))
        except Exception as e:
            print(f"Hesaplama hatası: {str(e)}")
            return None

    def _sanitize_expression(self, expression: str) -> str:
        """İfadeyi temizler ve normalleştirir."""
        return ''.join(c for c in expression if c.isascii()).strip()

    def _is_safe_expression(self, expression: str) -> bool:
        """İfadenin sadece izin verilen karakterleri içerip içermediğini kontrol eder."""
        allowed_chars = set('0123456789.+-*/() ^')
        return all(c in allowed_chars for c in expression)

    def _safe_functions(self) -> dict:
        """İzin verilen matematiksel fonksiyonların sözlüğünü döndürür."""
        return {
            'Decimal': Decimal,
            'pow': pow,
            'round': round
        }