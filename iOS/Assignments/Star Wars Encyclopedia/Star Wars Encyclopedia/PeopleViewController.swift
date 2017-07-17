//
//  ViewController.swift
//  Star Wars Encyclopedia
//
//  Created by MJ Norona on 7/17/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit
class PeopleViewController: UITableViewController {
    // Hardcoded data for now
    var people = [Any]()
    var gender = [Any]()
    var birth = [Any]()
    var mass = [Any]()
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        StarWarsModel.getAllPeople(completionHandler: { // passing what becomes "completionHandler" in the 'getAllPeople' function definition in StarWarsModel.swift
            data, response, error in
            do {
                // Try converting the JSON object to "Foundation Types" (NSDictionary, NSArray, NSString, etc.)
                if let jsonResult = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSDictionary {
                    if let results = jsonResult["results"] as? NSArray {
                        
                        for person in results {
                            let personDict = person as! NSDictionary
                            self.people.append(personDict["name"]! as! String)
                            self.gender.append(personDict["gender"]!)
                            self.birth.append(personDict["birth_year"]!)
                            self.mass.append(personDict["mass"]!)
                            
                        }
                    }
                }
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            } catch {
                print("Something went wrong")
            }
        })
    }
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "personSegue" {
            let indexPath = sender as! NSIndexPath
            
            let navigationController = segue.destination as! UINavigationController
            let personDescriptionViewController = navigationController.topViewController as! PersonDescriptionViewController
            
            personDescriptionViewController.name = self.people[indexPath.row] as! String
            personDescriptionViewController.gender = self.gender[indexPath.row] as! String
            personDescriptionViewController.birth = self.birth[indexPath.row] as! String
            personDescriptionViewController.mass = self.mass[indexPath.row] as! String
        }
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(indexPath.row)
        
        performSegue(withIdentifier: "personSegue", sender: indexPath)
        
    }
    
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
    }
    override func numberOfSections(in tableView: UITableView) -> Int {
        // if we return - sections we won't have any sections to put our rows in
        return 1
    }
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // return the count of people in our data array
        return people.count
    }
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // Create a generic cell
        let cell = UITableViewCell()
        // set the default cell label to the corresponding element in the people array
        cell.textLabel?.text = people[indexPath.row] as! String
        // return the cell so that it can be rendered
        return cell
    }
    
    @IBAction func unwindPerson(segue: UIStoryboardSegue) {
        
    }
}


