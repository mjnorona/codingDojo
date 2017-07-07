//
//  ViewController.swift
//  RaindbowRoad
//
//  Created by MJ Norona on 7/6/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    
    @IBOutlet weak var tableView: UITableView!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        tableView.dataSource = self
        tableView.rowHeight = 120
        print(tableView.contentSize.height)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

extension ViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 6
    }
    
    
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        
        let cell = tableView.dequeueReusableCell(withIdentifier: "MyCell", for: indexPath)
        if indexPath.row == 0 {
            cell.backgroundColor = UIColor.red
        } else if indexPath.row == 1 {
            cell.backgroundColor = UIColor.orange
        } else if indexPath.row == 2 {
            cell.backgroundColor = UIColor.yellow
        } else if indexPath.row == 3 {
            cell.backgroundColor = UIColor.green
        } else if indexPath.row == 4 {
            cell.backgroundColor = UIColor.blue
        } else if indexPath.row == 5 {
            cell.backgroundColor = UIColor.purple
        }
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat
    {
        return 100.0;//Choose your custom row height
    }
    
}

