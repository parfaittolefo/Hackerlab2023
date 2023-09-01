# Énoncé

<details><summary>Énoncé</summary>

**Pts: 100**

nc 54.37.70.250 1873

Author: unpasswd

File: [UTC_Server.py](https://gitlab.com/n4t10n/specifique-writeup/-/blob/main/Writeup_Hackerlab_Qualif_2023/Basic/Challenge%20file/UTC_server.py)

</details>

# Solution
<details><summary>Solution</summary>

Il s'agit d'une technique de chiffrement. Le point clé du challenge réside dans le bout de code suivant:

    t = int(time.time())
    random.seed(t)

`t`, la clé du chiffrement est la partie entière du _time stampe_ au démarage du script

[`random.seed(t)`](https://www.educative.io/answers/how-to-use-random-seed-method-in-python#:~:text=The%20random.,a%20random%20number%20in%20python.) permet d'initialiser les variables de sur lesuquelles se base la génération des nombre aléatoires. Celà signifie que nous auront les même nombre à chaque fois que nous initialisons ces variables sur la même valeur `t`. 

Et le problème est réglé

<img scr='img/utc1.png'>

**FLAG:** _CTF_R4nd1N7_15_N1C3_71479317491023!!_

File: [UTC_Solve.py](https://gitlab.com/n4t10n/specifique-writeup/-/blob/main/Writeup_Hackerlab_Qualif_2023/Basic/Challenge%20file/utc_solves.py)

</details>
