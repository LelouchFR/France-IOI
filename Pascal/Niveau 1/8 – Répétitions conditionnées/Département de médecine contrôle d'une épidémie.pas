program Solution;
var
   pop, contaminated, day: LongInt;
begin
   read(pop);
   contaminated := 1;
   day := 1;
   while contaminated < pop do
   begin
      day := day + 1;
      contaminated := contaminated * 3;
   end;
   writeln(day);
end.