//
//  FilmViewController.swift
//  Star Wars Encyclopedia
//
//  Created by MJ Norona on 7/17/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class FilmViewController: UITableViewController {
    
    var films = [Any]()
    var releaseDate = [Any]()
    var director = [Any]()
    var opening = [Any]()
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        StarWarsModel.getAllFilms(completionHandler: { // passing what becomes "completionHandler" in the 'getAllPeople' function definition in StarWarsModel.swift
            data, response, error in
            do {
                // Try converting the JSON object to "Foundation Types" (NSDictionary, NSArray, NSString, etc.)
                if let jsonResult = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSDictionary {
                    if let results = jsonResult["results"] as? NSArray {
                        print(results)
                        for film in results {
                            let filmDict = film as! NSDictionary
                            print(filmDict["release_date"])
                            self.films.append(filmDict["title"]! as! String)
                            self.releaseDate.append(filmDict["release_date"]! as! String)
                            self.director.append(filmDict["director"]! as! String)
                            self.opening.append(filmDict["opening_crawl"]! as! String)
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
        if segue.identifier == "filmSegue" {
            let indexPath = sender as! NSIndexPath
            
            let navigationController = segue.destination as! UINavigationController
            let filmDescriptionViewController = navigationController.topViewController as! FilmDescriptionViewController
            
            filmDescriptionViewController.film = films[indexPath.row] as! String
            filmDescriptionViewController.releaseDate = releaseDate[indexPath.row] as! String
            filmDescriptionViewController.director = director[indexPath.row] as! String
            filmDescriptionViewController.opening = opening[indexPath.row] as! String
        }
    }
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(indexPath.row)
        
        performSegue(withIdentifier: "filmSegue", sender: indexPath)
        
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
        return films.count
    }
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // Create a generic cell
        let cell = UITableViewCell()
        // set the default cell label to the corresponding element in the people array
        cell.textLabel?.text = films[indexPath.row] as! String
        // return the cell so that it can be rendered
        return cell
    }

    @IBAction func unwindFilm(segue: UIStoryboardSegue) {
        
    }
}
