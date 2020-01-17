Feature: test leaf

    Scenario Outline: modulo_edicion
        Given navegamos a la aplicacion de testleaf
            And damos click en el modulo edicion
        And llenamos el campo correo con "<email>"

    Examples:
    | email                      |
    | example@example.com        |
    | exampleexample@example.com |
    | example2@example.com       |
