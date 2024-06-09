
/* Creating Storeprocedure

delimiter //
create procedure SelectByCity(IN mycity varchar(20))
begin
	select * from student where City = mycity;
end //

delimiter ;
*/

/*
Calling StoredProcedure
call SelectByCity('Bellampally')
*/
################################################################################

/*
delimiter //
create procedure SelectByCityAndMarks(IN mycity varchar(20), IN mymarks int)
begin
	select * from student where City = mycity and Marks = mymarks;
end //

delimiter ;
*/


call SelectByCityAndMarks('Bellampally', 79);


