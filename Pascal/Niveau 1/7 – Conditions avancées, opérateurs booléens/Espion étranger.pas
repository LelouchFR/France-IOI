program Solution;
var
   startDate, endDate, entries, persons, i, date: LongInt;
begin
   read(startDate, endDate, entries);
   persons := 0;
   for i := 1 to entries do
   begin
      read(date);
      if (startDate <= date) and (date <= endDate) then
      begin
         persons := persons + 1;
      end;
   end;
   writeln(persons);
end.