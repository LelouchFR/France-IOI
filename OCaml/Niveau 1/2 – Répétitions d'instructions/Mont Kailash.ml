open Robot;;

for i = 1 to 108 do
  for j = 1 to 13 do
    haut();
  done;
  for j = 1 to 13 do
    droite();
  done;
  for j = 1 to 13 do
    bas();
  done;
  for j = 1 to 13 do
    gauche();
  done;
done;