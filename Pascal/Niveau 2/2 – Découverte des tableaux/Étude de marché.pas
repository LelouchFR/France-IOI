program Solution;
var
   prod: array of LongInt;
   prods, i, j, persons: LongInt;
begin
   read(prods);
   read(persons);
   setLength(prod, prods);
   for i := 0 to (prods - 1) do
   begin
      prod[i] := 0;
   end;
   for i := 1 to persons do
   begin
      read(j);
      prod[j] := prod[j] + 1;
   end;
   
   for i := 0 to (prods - 1) do
   begin
      writeln(prod[i]);
   end
end.