with my_cte as 
            (select email ,min(id) as id_to_keep
            from  Person group by Email
            )
            delete from Person
            where Id not in ( select id_to_keep from my_cte )
    