program Solution;
var
   column, row, i, j: LongInt;
begin
   row := 1;
   for i := 1 to 20 do
   begin
      column := 1;
      for j := 1 to 20 do
      begin
         write(column * row, ' ');
         column := column + 1;
      end;
      writeln;
      row := row + 1;
   end;
end.