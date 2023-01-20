open Robot;;    

for i = 1 to 20 do
  ramasser();
  for j = 1 to 15 do
    droite();
  done;
  deposer();
  for j = 1 to 15 do
    gauche();
  done;
done;