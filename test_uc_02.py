from src.vocab_game import VocabGame

class TestUC02InserirTentativa:
    def test_palpite_valido_5_letras(self):
        """CT-UC02-01: Palpite válido de 5 letras"""
        jogo = VocabGame()
        resultado = jogo.inserir_tentativa("CASAL")
        assert resultado == True
    
    def test_palpite_invalido_menos_5_letras(self):
        """CT-UC02-02: Palpite inválido - menos de 5 letras"""
        jogo = VocabGame()
        resultado = jogo.inserir_tentativa("ABC")
        assert resultado == False
    
    def test_palpite_invalido_mais_5_letras(self):
        """CT-UC02-03: Palpite inválido - mais de 5 letras"""
        jogo = VocabGame()
        resultado = jogo.inserir_tentativa("ABCDEF")
        assert resultado == False
    
    def test_palpite_invalido_caracteres_nao_alfabeticos(self):
        """CT-UC02-04: Palpite com caracteres não alfabéticos"""
        jogo = VocabGame()
        resultado = jogo.inserir_tentativa("A1C2E")
        assert resultado == False