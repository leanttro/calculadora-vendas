# Calculadora de Preços com Taxas Reais da InfinitePay

Este projeto é uma **calculadora de preços** que simula compras com **parcelamento** e **desconto à vista**, utilizando **valores reais de taxas** da **InfinitePay**.

A calculadora vai:
- **Adicionar um acréscimo de 3%** ao preço original do produto.
- **Aplicar um desconto de 3%** no valor final se o cliente pagar à vista no pix.
- **Simular o valor no pix ou com parcelamento em até 3x**, com juros conforme as taxas da InfinitePay:
  - **À vista no pix:** Desconto de **3%**.
  - **À vista 1x no cartão de crédito:** Juros de **4,20%**.
  - **Parcelado 2x no cartão de crédito:** Juros de **6,09%** por parcela.
  - **Parcelado 3x no cartão de crédito:** Juros de **7,01%** por parcela.

## Objetivo do projeto
- **Demonstrar** o cálculo de preços com acréscimos, descontos e juros para diferentes formas de pagamento.
- **Simular diferentes formas de pagamento** (à vista e parcelado).
- **Mostrar a transparência dos custos**, permitindo que o cliente saiba exatamente quanto ele pagará, considerando as taxas de parcelamento reais.

## Como usar
1. **Digite o valor do produto**.
2. Escolha a **opção de pagamento**:
   - **0** para pagamento via **pix** (à vista).
   - **1** para pagamento em **1x no cartão** (com juros de 4,20%).
   - **2** para pagamento em **2x no cartão** (com juros de 6,09% por parcela).
   - **3** para pagamento em **3x no cartão** (com juros de 7,01% por parcela).
3. A calculadora mostrará:
   - O **valor com o acréscimo de 3%** (para todos os tipos de pagamento).
   - O **desconto de 3%** no valor final se o pagamento for à vista (pix).
   - O **parcelamento em até 3x** com juros de:
     - **4,20%** para **1x no cartão**.
     - **6,09% por parcela** para **2x no cartão**.
     - **7,01% por parcela** para **3x no cartão**.

O cálculo será feito para cada forma de pagamento, mostrando o valor final de acordo com a escolha do cliente.

## Tecnologias Usadas
- Python

## Como rodar o código
1. **Baixe o repositório** ou **clone** o projeto.
2. Abra o terminal ou seu ambiente de desenvolvimento preferido.
3. Execute o script com o comando:
```bash
python calculadora-vendas.py
