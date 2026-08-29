package br.com.exemplo.beneficios.controller;

import br.com.exemplo.beneficios.entity.Transacao;
import br.com.exemplo.beneficios.repository.TransacaoRepository;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/transacoes")
public class TransacaoController {

    private final TransacaoRepository repository;

    public TransacaoController(TransacaoRepository repository) {
        this.repository = repository;
    }

    @PreAuthorize("hasRole('OPERADOR')")
    @GetMapping("/relevantes")
    public List<Transacao> relevantes() {
        return repository.ativasRelevantes();
    }
}
