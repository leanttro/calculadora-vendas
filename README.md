# Calculadora de Preços com Taxas Reais da InfinitePay

Este projeto é uma **calculadora de preços** que simula compras com **parcelamento** e **desconto à vista**, utilizando **valores reais de taxas** da **InfinitePay**.

A calculadora vai:
- **Adicionar um acréscimo de 3%** ao preço original do produto.
- **Aplicar um desconto de 3%** no valor final se o cliente pagar à vista.
- **Simular o parcelamento em até 3x**, com juros conforme as taxas da InfinitePay:
  - **À vista:** Desconto de **4,20%**.
  - **2x:** Juros de **6,09%** por parcela.
  - **3x:** Juros de **8,40%** por parcela.

## Objetivo do projeto
- **Demonstrar** o cálculo de preços com acréscimos, descontos e juros para diferentes formas de pagamento.
- **Simular diferentes formas de pagamento** (à vista e parcelado).
- **Mostrar a transparência dos custos**, permitindo que o cliente saiba exatamente quanto ele pagará, considerando as taxas de parcelamento reais.

## Como usar
1. **Digite o valor do produto**.
2. A calculadora mostrará:
   - O **valor com o acréscimo de 3%**.
   - O **desconto de 4,20%** caso o pagamento seja à vista.
   - O **parcelamento em até 3x** com juros de **6,09% por parcela para 2x** e **8,40% para 3x**.
3. O cálculo será feito para cada forma de pagamento, mostrando o valor final em cada caso.

## Tecnologias Usadas
- Python

## Como rodar o código
1. Baixe o repositório ou clone.
2. Abra o terminal ou seu ambiente de desenvolvimento.
3. Execute o script com o comando:  
```bash
python calculadora-vendas.py
