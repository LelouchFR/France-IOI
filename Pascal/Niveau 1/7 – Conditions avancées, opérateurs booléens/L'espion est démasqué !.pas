program Solution;
var
   nbPersonnes, nbCriteres: LongInt;
   size, age, weight, horse, brownHair: LongInt;
   loop: LongInt;
begin
   read(nbPersonnes);
   for loop := 1 to nbPersonnes do
   begin
      nbCriteres := 0;
      read(size);
      if (178 <= size) and (size <= 182) then
      begin
         nbCriteres := nbCriteres + 1;
      end;
      read(age);
      if age >= 34 then
      begin
         nbCriteres := nbCriteres + 1;
      end;
      read(weight);
      if weight < 70 then
      begin
         nbCriteres := nbCriteres + 1;
      end;
      read(horse);
      if horse = 0 then
      begin
         nbCriteres := nbCriteres + 1;
      end;
      read(brownHair);
      if brownHair = 1 then
      begin
         nbCriteres := nbCriteres + 1;
      end;   
      
      if nbCriteres = 0 then
      begin
         writeln('Impossible');
      end
      else if nbCriteres = 5 then
      begin
         writeln('Très probable');
      end
      else if nbCriteres >= 3 then
      begin
         writeln('Probable');
      end
      else
      begin
         writeln('Peu probable');
      end 
   end;
end.