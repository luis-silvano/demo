package br.com.exemplo.beneficios.repository;

import br.com.exemplo.beneficios.entity.Transacao;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface TransacaoRepository extends JpaRepository<Transacao, Long> {

    /** Transacoes ativas acima do piso de materialidade usado na conciliacao diaria. */
    @Query("""
        select t from Transacao t
        where t.status = 'ATIVA'
          and t.valor > 100
        order by t.dataMovimento desc
        """)
    List<Transacao> ativasRelevantes();
}
