{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#estructura selectiva\n",
    "#Programa que leera dos numeros ingresados y determinara cual es mayor o si son iguales.\n",
    "a1=int(input(\"numero 1\")\n",
    "a2=int(input(\"numero 2')\n",
    "if a1==a2:\n",
    "             print (\"son iguales\")\n",
    "elif a1>a2:\n",
    "             print (\"a1 es mayor que a2\")\n",
    "elif a2<a1:\n",
    "             print (\"a2 es mayor que a1\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#estructura iterativa\n",
    "#Este programa se repetirá 5 veces o hasta que se ingresla palabra \"estructural\" y desplegará el número de intentos hasta que \n",
    "#se ingrese la palabra.\n",
    "\n",
    "entrada = \"\"\n",
    "suma = 0\n",
    "while suma < 5 and entrada != \"estructural\":\n",
    "    entrada = input(\"Clave: \")\n",
    "    suma += 1\n",
    "    print(\"Intento %d. \\n \" % suma)\n",
    "print(\"Utilizaste %d intentos.\" % suma)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intento 1.\n",
      "Clave: estructural\n",
      "\n",
      "Intento 2.\n",
      "Clave: estructural\n",
      "\n",
      "Intento 3.\n",
      "Clave: estructural\n",
      "\n",
      "Tuviste 0 intentos fallidos.\n"
     ]
    }
   ],
   "source": [
    "#estructura secuencial con una estructura selectiva dentro de una iterativa\n",
    "#Este programa se repetirá 5 veces y desplegará el número de intentos en los\n",
    "#que se ingresó la palabra \"estructural\".\n",
    "\n",
    "entrada = \"\"\n",
    "suma = 0\n",
    "fallido = 0\n",
    "while suma < 5:\n",
    "    suma += 1\n",
    "    print(\"Intento %d.\" % suma)\n",
    "    entrada = input(\"Clave: \")\n",
    "    print()\n",
    "\n",
    "    if entrada == \"estructural\":\n",
    "        continue\n",
    "        \n",
    "    fallido += 1\n",
    "print(\"Tuviste %d intentos fallidos.\" % fallido)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
