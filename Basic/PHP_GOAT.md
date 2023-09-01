Voici le contexte

<img src='img/php1.png'>

Une fois sur liste, nous avons cette calculatrice qui nous permet de faire des calculs basics
<img src='img/php2.png'>

Essayons de voir le code source
<img src='img/php3.png'>

On remarque la fonction **eval()**. Après quelques recherches, on découvre que cette dernière permet d'exécuter du code php comme s'il s'agissait d'une partie du programme. Du coup lorsqu'on essait **system("ls")** on obtient le résultat suivant
<img src='img/php4.png'>

Super !!! On arrive à lister les fichiers du répertoire courant. Maintenant il nous suffit de faire **system("cat FLAG_07314077310473014032840914317407104318403173014717430")** Et on obtient le flag
<img src='img/php5.png'>

FLAG: **CTF_PHP_S0URc3_c0D3_4M4Z1NG_9741926**
