import csv

input_file = 'students.csv'        
failed_file = 'failed_students.csv'
passed_file = 'passed_students.csv'

with open(input_file, 'r', newline='') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    with open(failed_file, 'w', newline='') as failfile,\
         open(passed_file, 'w', newline='') as passfile:

        failed_writer = csv.DictWriter(failfile, fieldnames=fieldnames)
        passed_writer = csv.DictWriter(passfile, fieldnames=fieldnames)

        failed_writer.writeheader()
        passed_writer.writeheader()

        for row in reader:
            try:
                grade = int(row['Grade'])
            except ValueError:
                continue

            if grade < 50:
                failed_writer.writerow(row)
            else:
                passed_writer.writerow(row)
    



     

    
      
   
 



   
            
            
            

        

    
    

    