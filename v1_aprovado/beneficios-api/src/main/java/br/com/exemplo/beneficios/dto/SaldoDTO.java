package br.com.exemplo.beneficios.dto;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Positive;

import java.math.BigDecimal;

public class SaldoDTO {

    @NotNull
    private Long cartaoId;

    @NotNull
    @Positive
    private BigDecimal saldoDisponivel;

    @NotNull
    private BigDecimal saldoBloqueado;
}
