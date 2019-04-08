# Grub
	« DebWorkManager » est un programme avec interface graphique qui va permettre d’accéder à distance aux ordinateurs cibles afin d’y configurer des routes, des règles iptables et d’afficher les logs de ces machines distantes.

	 Le fonctionnement repose sur l’édition de deux scripts ( iptables_init.sh et route_init.sh ) qui seront déployés sur l’ordinateur cible dans le répertoire de démarrage init.d. Les machines distantes ( utilisateur + IP ) sont sauvegardées dans une base de donnée SQL ainsi que les chemins vers les logs souhaités. 

Prérequis 

côté serveur : 

    • L’exécution du programme se fait sous Linux Debian,
    • Installer la librairie python ( tkinter ),
    • Installer sshpass, 
    • S’assurer que le pare feu ne bloque pas les connexions SSH, 
    • Installer « openssh-client » et  « openssh-server ».


côté client :

    • Les machines clientes doivent avoir un OS sous linux Debian,
    • Dans le fichier etc/ssh/sshd_config modifier PermitRootLogin no en PermitRootLogin yes,
      ( solution temporaire qui entraîne une faille de sécurité potentielle, cette fonctionnalité sera modifiée rapidement )
    • S’assurer que le pare feu ne bloque pas les connexions SSH, 
    • Installer « openssh-client » et  « openssh-server ».

Comment ça marche ???

    • Afin de vous apporter une aide pour utiliser se programme ou en comprendre le fonctionnement, j’ai réalisé une documentation technique que vous trouverez en lançant DebWorkManager puis en cliquand sur l’onglet « aide »



