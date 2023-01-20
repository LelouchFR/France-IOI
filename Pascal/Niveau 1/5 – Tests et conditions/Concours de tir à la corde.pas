program Solution;
var
   persons, i, tot1, tot2, p1, p2: LongInt;
begin
   read(persons);
   tot1 := 0;
   tot2 := 0;
   for i := 1 to persons do
   begin
      read(p1, p2);
      tot1 := tot1 + p1;
      tot2 := tot2 + p2;
   end;
   if tot1 > tot2 then
   begin
      writeln('L''équipe 1 a un avantage');
   end
   else
   begin
      writeln('L''équipe 2 a un avantage');
   end;
   writeln('Poids total pour l''équipe 1 : ', tot1);
   writeln('Poids total pour l''équipe 2 : ', tot2);  
end. 