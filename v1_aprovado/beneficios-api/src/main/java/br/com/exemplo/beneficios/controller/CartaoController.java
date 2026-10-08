package br.com.exemplo.beneficios.controller;

import br.com.exemplo.beneficios.dto.SaldoDTO;
import br.com.exemplo.beneficios.service.PagamentoService;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

/**
 * Consulta de cartao e saldo de beneficios.
 * Acesso restrito ao papel OPERADOR (dado sensivel de titular).
 */
@RestController
@RequestMapping("/api/cartoes")
public class CartaoController {

    private final PagamentoService service;

    public CartaoController(PagamentoService service) {
        this.service = service;
    }

    @GetMapping("/{id}/saldo")
    public SaldoDTO consultarSaldo(@PathVariable Long id) {
        return service.consultarSaldo(id);
    }

    @PreAuthorize("hasRole('SUPERVISOR')")
    @PostMapping("/{id}/bloqueio")
    public void bloquear(@PathVariable Long id, @RequestParam String motivo) {
        service.bloquearCartao(id, motivo);
    }
}
