open Robot;;

haut();
for i = 1 to 4 do
  for j = 1 to 8 do
    haut();
  done;
  droite();
  for j = 1 to 8 do
    bas();
  done;
  droite();
done;
for loop = 1 to 8 do
  haut();
done;
droite();
for loop = 1 to 9 do
  bas();
done;
for loop = 1 to 9 do
  gauche();
done;