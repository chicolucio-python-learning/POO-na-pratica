# Raio-X da Programação Orientada a Objetos

Anotações do curso

## Os paradigmas da programação

Os níveis de programação:
- baixo: bits, bytes, fluxo de elétrons. 0 e 1. Dados, apenas valores.
- alto: ser humano. Símbolos, ideias. Possuem significado.

Para juntas os dois níveis, criamos camadas de abstrações. Assim, fica mais fácil a comunicação com a máquina usando uma forma mais próxima a compreensão humana.

As abstrações são conhecidas como Paradigmas de Programação. São as diferentes abordagens utilizadas para a situação. Tipos:

- imperativo: ordens e comandos. Baixo nível.
- procedural: com subrotinas que fazem condições específicas. If e go to.
- estruturado: estruturas de controle de fluxo. Variáveis locais. While e for.
- funcional: expressões e funções.
- orientado a objetos: organizar e dados e código numa mesma entidade.
- multi-paradigmas: exemplo do Python

### Dados vs objetos

- Dados: apenas valor
- Objetos: valor, identidade e tipo

## Demonstração

```python
>>> int(0b1000001)
65
>>> chr(0b1000001)
'A'
```

O mesmo conjunto de bits dependendo do contexto pode ter diferentes valores.

```python
>>> foods = ['apple', 'orange', 'cat']
>>> foods
['apple', 'orange', 'cat']  # valor
>>> id(foods)
139849151764224  # identidade
>>> type(foods)
list  # tipo

>>> bag = ['apple', 'orange', 'cat']
>>> bag
['apple', 'orange', 'cat']
>>> id(bag)
139849152527360
>>> type(bag)
list

>>> foods, bag
(['apple', 'orange', 'cat'], ['apple', 'orange', 'cat'])

>>> foods == bag  # comparação de valores
True
>>> foods is bag  # verificando se são o mesmo objeto
False

>>> id(foods), id(bag)
(139849151764224, 139849152527360)

>>> type(foods)
list  # retorna a própria classe e não uma string

>>> cls = type(foods)  # criando uma referência para a classe list
>>> cls
list
>>> cls((1, 2, 3))
[1, 2, 3]
```

## Alan Kay

> I thought of objects being like biological cells and/or individual computers on a network, only able to communicate with messages

Ou seja, o importante é a troca de mensagens, como os objetos se relacionam. É importante definir uma interface de comunicação.

- everything is an object
- objects communicate by sending and receiving messages
- objects have their own memory (conhecem seu próprio estado, não é global)
- every object is an instance of a class
- the class holds the shared behavior for its instances

Objeto é o organismo vivo, a classe é o DNA. Na classe há os métodos que podem utilizados pelo objeto.

## Classes, atributos e métodos no Python

```python
>>> class Car: pass
>>> Car      # objeto, variável que referência o objeto car em memória
__main__.Car
>>> Car()    # instanciando a classe
<__main__.Car at 0x7fabbd3b7e50>
>>> type(Car())
__main__.Car
>>> type(Car)
type
>>> issubclass(Car, object)  # em Python 3, toda classe é subclasse de object
True

# As duas linhas seguintes são equivalentes
>>> class Car(object): pass
>>> class Car: pass

# Em Python, class também é um comando executável, não apenas uma instrução declarativa
>>> class Car:
...     print('Loading a class...')
...     name = 'Ferrari'
...     print('Done defining a ' + name + '!' * 5)
...     for char in name:
...         print(char.upper())
...     if int(len(name) % 2) == 0:
...         portas = 2
...     else:
...         portas = 3
...     print(portas)
...
Loading a class...
Done defining a Ferrari!!!!!
F
E
R
R
A
R
I
3

# As variáveis locais definidas no corpo da classe são atributos de classe

>>> Car
__main__.Car
>>> Car.name, Car.portas  # atributos de classe
('Ferrari', 3)
>>> c = Car()
>>> c.name, c.portas  # verifica se a instância possui e, não possuindo, vai para a classe
('Ferrari', 3)

>>> c.name = 'BMW'
>>> c.portas = 2
>>> c.name, c.portas
('BMW', 2)
>>> Car.name, Car.portas
('Ferrari', 3)

# Atributos de instância não sobrescrevem a classe
>>> d = Car()
>>> d.name, d.portas
('Ferrari', 3)
>>> Car.name, c.name, d.name
('Ferrari', 'BMW', 'Ferrari')

>>> d.name = 'Audi'
>>> Car.name, c.name, d.name
('Ferrari', 'BMW', 'Audi')
>>> del c.name
>>> Car.name, c.name, d.name
('Ferrari', 'Ferrari', 'Audi')

# Agora mudando na classe
>>> Car.name = 'Fiat'
>>> Car.name, c.name, d.name
('Fiat', 'Fiat', 'Audi')

# verificando os atributos de classe
>>> Car.__dict__
mappingproxy({'__module__': '__main__',
              'name': 'Fiat',
              'char': 'i',
              'portas': 3,
              '__dict__': <attribute '__dict__' of 'Car' objects>,
              '__weakref__': <attribute '__weakref__' of 'Car' objects>,
              '__doc__': None})

# Verificando as instâncias
>>> c.__dict__
{'portas': 2}
>>> d.__dict__
{'name': 'Audi'}
>>> c.portas
2
>>> d.portas
3

# verifica na instância e depois na classe
>>> c.xpto
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-32-4abf047eb710> in <module>
----> 1 c.xpto

AttributeError: 'Car' object has no attribute 'xpto'

# o acessor (ponto) já possui a lógica para fazer a pesquisa dos atributos
>>> c.__class__
__main__.Car
>>> c.__dict__
{'portas': 2}
>>> c.name
'Fiat'
>>> c.__class__.name
'Fiat'

# Implementando o construtor da classe
>>> class Car:
...     name = 'Ferrari'  # atributo de classe
...     def __init__(self, model):
...         self.model = model  # atributo de instância
...
>>> Car()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-38-6398cfbfe55d> in <module>
----> 1 Car()

TypeError: __init__() missing 1 required positional argument: 'model'

>>> c, d = Car('F50'), Car('F40')
>>> c.name, d.name
('Ferrari', 'Ferrari')
>>> c.model, d.model
('F50', 'F40')

>>> hasattr(Car, 'model')
False
>>> Car.model = 'TopGear'  # injetando atributo model
>>> Car.model, c.model, d.model
('TopGear', 'F50', 'F40')
>>> del c.model
>>> Car.model, c.model, d.model
('TopGear', 'TopGear', 'F40')

>>> Car.__dict__
mappingproxy({'__module__': '__main__',
              'name': 'Ferrari',
              '__init__': <function __main__.Car.__init__(self, model)>,
              '__dict__': <attribute '__dict__' of 'Car' objects>,
              '__weakref__': <attribute '__weakref__' of 'Car' objects>,
              '__doc__': None,
              'model': 'TopGear'})
>>> c.__dict__
{}
>>> d.__dict__
{'model': 'F40'}

>>> class Car:
...     name = 'Ferrari'
...     def ignition(self):
...         print('vrummm...')
...         self.motor_running = True
...

>>> c = Car()
>>> c.ignition()
>>> c.motor_running
True
>>> d = Car()
>>> d.motor_running
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-55-fa664c51c529> in <module>
----> 1 d.motor_running

AttributeError: 'Car' object has no attribute 'motor_running'

# o construtor impede esse tipo de inconsistência no estado do objeto
>>> class Car:
...     name = 'Ferrari'
...     def __init__(self):
...         self.motor_running = False
...     def ignition(self):
...         self.motor_running = True
...         print('vrummm...')
...

>>> c = Car()
>>> c.motor_running
False
>>> c.ignition()
>>> c.motor_running
True

# logo um método nada mais é do que uma função definida no corpo da classe
>>> d = Car()
>>> d.motor_running
False


>>> Car.ignition(d)  # é isso que o sugar syntax d.ignition() faz, daí o self
vrummm...

>>> Car.ignition
<function __main__.Car.ignition(self)>
>>> d.ignition
<bound method Car.ignition of <__main__.Car object at 0x7fabbc3e49d0>>
>>> d.motor_running = False
>>> d.__dict__
{'motor_running': False}

>>> m = d.ignition
>>> m
<bound method Car.ignition of <__main__.Car object at 0x7fabbc3e49d0>>
>>> m.__
>>> m.__class__
method
>>> type(m)
method

# a junção de __call__ com __func__ e __self__ é que permite a execução do objeto método
>>> m.__func__
<function __main__.Car.ignition(self)>
>>> m.__self__
<__main__.Car at 0x7fabbc3e49d0>
>>> m()  # chama o __call__, equivale a d.ignition() que equivale a Car.ignition(d)
>>> d.motor_running
True
>>> m.__func__(m.__self__)
vrummm...
   
>>> d.motor_running
True

>>> d = Car()
>>> d.motor_running
False
>>> def f(g):
...     g()
...
>>> f(d.ignition)  # passando o objeto para a função, da instância d
vrummm... 

>>> d.motor_running
True
```

## Herança

```python
>>> class Car:
...     portas = 2  # atributo de classe
...     def __init__(self, name):
...         self.name = name  # atributo de instância
...
>>> class Ferrari(Car):
...     def __init__(self, model):
...         super().__init__('Ferrari')  # construtor da classe base. Obrigatório
...         self.model = model  # atributo de instância
...
>>> f = Ferrari('F50')
>>> f. name  # atributo de instância
'Ferrari'
>>> f.model  # atributo de instância
'F50'
>>> f.portas  # atributo de classe
2

>>> f.__dict__
{'name': 'Ferrari', 'model': 'F50'}
>>> Ferrari.__dict__
mappingproxy({'__module__': '__main__',
              '__init__': <function __main__.Ferrari.__init__(self, model)>,
              '__doc__': None})
>>> Car.__dict__
mappingproxy({'__module__': '__main__',
              'portas': 2,
              '__init__': <function __main__.Car.__init__(self, name)>,
              '__dict__': <attribute '__dict__' of 'Car' objects>,
              '__weakref__': <attribute '__weakref__' of 'Car' objects>,
              '__doc__': None})
```