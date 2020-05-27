Diagram:
----------------------

![Alt text](img/v.png?raw=true "Diagram")

Softwares necessários:
----------------------

1 - Python 2.7.16

2 - O Coap Server utilizado foi o CoAPthon versão 4.0.2

>> sudo pip install CoAPthon

Como executar os testes:
----------------------

1 - Para rodar os testes primeiro é necessário estar com o SenseHat aberto 

2 - Rodar o Servidor Coap

>> python server.py 192.168.0.150 5683

Parâmetros

1 - 192.168.0.150 ip do servidor coap
2 - 5683 porta

Aparecerá escrito "Add New Sensor", Digite o ID do sensor, por exmeplo S2; O ID do sensor S1 já foi criado por padrão

Outro recurso que foi automaticamente criado foi o /atuador

3 - Rode o atuador (na mesma vm onde está o SensHat)

>> python atuador.py 192.168.0.150 568

Todos os leds devem ficar em branco

4 -Em um outro terminal rode o script que será a aplicação que sabe quais são os limites
de um sensor específico e fará um post no /atuador que acenderá o led específico

>> python app.py 192.168.0.150 5683 S1 10 10 10

Parâmetros

- S1 nome do recurso
- 10 led que será acesso
- 10 humidade
- 10 temperatura

5 - Precisamos inserir um valor no recurso S1 do CoaP Server, abra outro terminar e execute 

>> python sensor_simulator.py -o PUT -p coap://192.168.0.150:5683/s1 -P 20-30

>> python sensor_simulator.py -o PUT -p coap://192.168.0.150:5683/s2 -P 10-30

Veja que o led 10 acendeu e o 20 ficou apagado pois a temperatura de S2 é 10. Se mudar a temp de S2
para 21 vai acender o led 20
