program Solution;
var
   start, ends, i, tot: LongInt;
begin
   read(start);
   read(ends);
   tot := 0;
   for i := 1 to start do
   begin
      if start >= ends then
      begin
         tot := tot + start * start;
         start := start - 1;
      end;
   end;
   writeln(tot);
end.