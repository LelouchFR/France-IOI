program Solution;
var
   DDP, DFP, DDS, DFS: LongInt;
begin
   read(DDP, DFP, DDS, DFS);
   if (DFS < DDP) or (DFP < DDS) then
   begin
      writeln('Pas amis');
   end
   else
   begin
      writeln('Amis')
   end;
end.