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
    
    func tableViewHeight() -> CGFloat {
        tableView.layoutIfNeeded()
        
        return tableView.contentSize.height
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let rand = Int(arc4random_uniform(91) + 5)
        var cell = tableView.dequeueReusableCell(withIdentifier: "reuseIdentifier")
        if cell == nil {
            cell = UITableViewCell(style: .value1, reuseIdentifier: "reuseIdentifier")
        }
        cell?.textLabel?.text = "\(names[indexPath.row])"
        cell?.detailTextLabel?.text = "\(rand) years old"
        
        return cell!
    }
}

