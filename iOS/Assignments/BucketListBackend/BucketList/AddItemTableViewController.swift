//
//  AddItemTableViewController.swift
//  BucketList
//
//  Created by MJ Norona on 7/10/17.
//  Copyright © 2017 MJ Norona. All rights reserved.
//

import UIKit

class AddItemTableViewController: UITableViewController {
    weak var delegate: AddItemTableViewControllerDelegate?
    var item: NSDictionary?
    var text: String?
    var indexPath: NSIndexPath?
    
    
    @IBOutlet weak var itemTextField: UITextField!
    
    
    @IBAction func cancelButtonPressed(_ sender: UIBarButtonItem) {
        delegate?.cancelButtonPressed(by: self)
    }
    
    @IBAction func saveButtonPressed(_ sender: UIBarButtonItem) {
        
        let id = item?["pk"] as! Int
        self.text = itemTextField.text!
        delegate?.itemSaved(by: self, with: self.text!, index: id, at: indexPath)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if indexPath != nil {
            let field = item?["fields"] as! NSDictionary
            let objective = field["objective"] as! NSString
            itemTextField.text = objective as! String
        } else {
            itemTextField.text = ""
        }
        

    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }




}
