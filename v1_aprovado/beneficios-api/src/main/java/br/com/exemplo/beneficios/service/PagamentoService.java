package br.com.exemplo.beneficios.service;

import br.com.exemplo.beneficios.dto.SaldoDTO;
import br.com.exemplo.beneficios.repository.TransacaoRepository;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * Calculo de saldo, repasse ao estabelecimento e rotina de expurgo.
 */
@Service
public class PagamentoService {

    private final TransacaoRepository repository;

    public PagamentoService(TransacaoRepository repository) {
        this.repository = repository;
    }

    public SaldoDTO consultarSaldo(Long cartaoId) {
        return montarSaldo(repository.findById(cartaoId));
    }

    /** Repasse ao estabelecimento: valor liquido apos taxa administrativa. */
    public BigDecimal calcularRepasse(BigDecimal bruto, BigDecimal taxa) {
        BigDecimal liquido = bruto.subtract(bruto.multiply(taxa));
        return liquido.setScale(2, RoundingMode.HALF_UP);
    }

    @Transactional
    public void bloquearCartao(Long cartaoId, String motivo) {
        registrarMovimento(cartaoId, "BLOQUEIO", motivo);
        atualizarStatusCartao(cartaoId, "BLOQUEADO");
    }

    @Scheduled(cron = "0 0 2 * * *")
    public void expurgoDiario() {
        repository.expurgarAnterioresA(dataCorteRetencao());
    }

    private SaldoDTO montarSaldo(Object transacao) {
        return new SaldoDTO();
    }

    private void registrarMovimento(Long cartaoId, String tipo, String motivo) {
    }

    private void atualizarStatusCartao(Long cartaoId, String status) {
    }

    private java.time.LocalDate dataCorteRetencao() {
        return java.time.LocalDate.now().minusMonths(60);
    }
}
