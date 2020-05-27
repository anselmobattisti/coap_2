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

Aparecerá escrito "Add New Sensor", Digite o ID do sensor, por exmeplo S2; O ID do sensor S1 já foi criado por padrão

3 - Rode o atuador

>> python atuador.py 192.168.0.150 568

Todos os leds devem ficar em branco

4 -Em um outro terminal rode o script que será o cliente e fará recebe a temperatura do sendor e faz um post no /atuador que acenderá os leds

>> python app.py 192.168.0.150 5683 S1 10 10

# S1 nome do recurso
# 10 temperatura
# 10 led que será acesso

<<<<<<< HEAD:Readme
>> python app.py 192.168.0.150 5683 S2 20 20

5 - Precisamos inserir um valor no recurso S1 do CoaP Server, abra outro terminar e execute 

>> python sensor_simulator.py -o PUT -p coap://localhost:5683/S1 -P 55

>> python sensor_simulator.py -o PUT -p coap://localhost:5683/S2 -P 10

Veja que o led 10 acendeu e o 20 ficou apagado pois a temperatura de S2 é 10. Se mudar a temp de S2
para 21 vai acender o led 20
=======
Cada cliente está lendo o seu recurso específico no servidor Coap
>>>>>>> db0054a97eb2557e048cdf03134850155fba5b77:README.md