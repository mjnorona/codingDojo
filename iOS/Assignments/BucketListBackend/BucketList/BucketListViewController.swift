//
//  ViewController.swift
//  BucketList
//
//  Created by MJ Norona on 7/10/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit
import CoreData

class BucketListViewController: UITableViewController, AddItemTableViewControllerDelegate {

    var items = [NSDictionary]()
    
    
    
    override func viewDidLoad() {
        TaskModel.getAllTasks() {
            data, response, error in
            do {
                if let tasks = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSArray {
                    for i in 0..<tasks.count {
                        let item = tasks[i] as! NSDictionary
                        
                        self.items = tasks as! Array
                    }
                }
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            } catch {
                print("Something went wrong")
            }
        }
        super.viewDidLoad()
    }
    
    override func viewDidAppear(_ animated: Bool) {
        TaskModel.getAllTasks() {
            data, response, error in
            do {
                if let tasks = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSArray {
                    for i in 0..<tasks.count {
                        let item = tasks[i] as! NSDictionary
                        
                        self.items = tasks as! Array
                    }
                }
                DispatchQueue.main.async {
                    self.tableView.reloadData()
                }
            } catch {
                print("Something went wrong")
            }
        }
        super.viewDidAppear(true)
        
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        
        return items.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "ListCell", for: indexPath)
        let item = items[indexPath.row]
        let field = item["fields"] as! NSDictionary
        let objective = field["objective"] as! NSString
        cell.textLabel?.text = objective as String
        return cell
    }
   
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print("Selected")
    }
    
    override func tableView(_ tableView: UITableView, accessoryButtonTappedForRowWith indexPath: IndexPath) {
        performSegue(withIdentifier: "EditItemSegue", sender: indexPath)
    }
    
//    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
//        let item = items[indexPath.row]
//        managedObjectContext.delete(item)
//        
//        do {
//            try managedObjectContext.save()
//        } catch {
//            print("\(error)")
//        }
//        items.remove(at: indexPath.row)
//        tableView.reloadData()
//        
//    }
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        var type = (sender is IndexPath ? true : false)
        let navigationController = segue.destination as! UINavigationController
        let addItemTableViewController = navigationController.topViewController as! AddItemTableViewController
        addItemTableViewController.delegate = self
        
        if type == true{
            let indexPath = sender as! NSIndexPath
            
            
            let item = items[indexPath.row]
            addItemTableViewController.item = item
            
            addItemTableViewController.indexPath = indexPath
        }
        
    }
    
//    func fetchAllItems() {
//        let request = NSFetchRequest<NSFetchRequestResult>(entityName: "BucketListItem")
//        do {
//            let result = try managedObjectContext.fetch(request)
//            items = result as! [String]
//        } catch {
//            print("\(error)")
//        }
//    }
    
    func cancelButtonPressed(by controller: AddItemTableViewController) {
        print("I'm the hidden controller, BUT iam responding to the cancel on the top view controller.")
        dismiss(animated: true, completion: nil)
    }
    
    func itemSaved(by controller: AddItemTableViewController, with text: String, index: Int?, at indexPath: NSIndexPath?) {
//        if let ip = indexPath{
//            let item = items[ip.row]
//            item = text
//        } else {
//            let item = NSEntityDescription.insertNewObject(forEntityName: "BucketListItem", into: managedObjectContext) as! BucketListItem
//            item.text = text
//            items.append(item)
//        }
//        
//        do {
//            try managedObjectContext.save()
//        } catch {
//            print("\(error)")
//        }
        if let ip = indexPath {
            
            
            TaskModel.updateTaskWithObjective(objective: text, id: index!,completionHandler: {
                data, response, error in
                do {
                    if let task = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSArray {
                        print("going here")
                        self.items.append(task[0] as! NSDictionary)
                    }
                    
                } catch let err as NSError {
                    print("Something went wrong",err)
                }
            })
            
        } else {
            print("goes here")
            TaskModel.addTaskWithObjective(objective: text, completionHandler: {
                data, response, error in
                do {
                    if let task = try JSONSerialization.jsonObject(with: data!, options: JSONSerialization.ReadingOptions.mutableContainers) as? NSArray {
                        print("going here")
                        self.items.append(task[0] as! NSDictionary)
                    }
                    
                } catch let err as NSError {
                    print("Something went wrong",err)
                }
            })
        }
        
        
        
        
        
        dismiss(animated: true, completion: nil)
        
    }
}

