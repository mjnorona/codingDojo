//
//  ViewController.swift
//  AgingPeople
//
//  Created by MJ Norona on 7/6/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var names = ["MJ", "Marcus", "Norona", "Jazz", "Gemma", "Paciencia", "Bill", "Bob", "James", "Jeremy", "John", "Jacob"]

    @IBOutlet weak var tableView: UITableView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        tableView.dataSource = self
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

extension ViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return names.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let rand = Int(arc4random_uniform(91) + 5)
        let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
        cell.textLabel?.text = "\(names[indexPath.row]) \(rand) years old"
        cell.detailTextLabel?.text = String(indexPath.row)
        
        return cell
    }
}

