package com.todo.entity;

import java.awt.*;
import java.awt.event.*;
import java.sql.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class TodoGUI extends JFrame {

    private JTextField titleField, descriptionField, statusField, dueDateField;
    private JButton addButton, deleteButton, updateButton, viewButton;
    private JTable tasksTable;
    private Connection connection;

    public TodoGUI() {
        // Set up the frame
        setTitle("To-Do List");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Centering the JFrame on screen
        setLocationRelativeTo(null); // This will center the frame

        // Set the layout to GroupLayout for better alignment of components
        GroupLayout layout = new GroupLayout(getContentPane());
        getContentPane().setLayout(layout);

        // Create components
        JLabel titleLabel = new JLabel("Title:");
        titleField = new JTextField(20);
        JLabel descriptionLabel = new JLabel("Description:");
        descriptionField = new JTextField(20);
        JLabel statusLabel = new JLabel("Status (pending/completed):");
        statusField = new JTextField(10);
        JLabel dueDateLabel = new JLabel("Due Date (YYYY-MM-DD):");
        dueDateField = new JTextField(10);

        addButton = new JButton("Add Task");
        deleteButton = new JButton("Delete Task");
        updateButton = new JButton("Update Task Status");
        viewButton = new JButton("View All Tasks");

        // Set up JTable
        tasksTable = new JTable();
        JScrollPane scrollPane = new JScrollPane(tasksTable);

        // Layout Grouping
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(true);

        // Horizontal group
        layout.setHorizontalGroup(
            layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                .addGroup(layout.createSequentialGroup()
                    .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                        .addComponent(titleLabel)
                        .addComponent(descriptionLabel)
                        .addComponent(statusLabel)
                        .addComponent(dueDateLabel))
                    .addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
                        .addComponent(titleField)
                        .addComponent(descriptionField)
                        .addComponent(statusField)
                        .addComponent(dueDateField)
                        .addComponent(addButton)
                        .addComponent(deleteButton)
                        .addComponent(updateButton)
                        .addComponent(viewButton))
                )
                .addComponent(scrollPane)
        );

        // Vertical group
        layout.setVerticalGroup(
            layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(titleLabel)
                    .addComponent(titleField))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(descriptionLabel)
                    .addComponent(descriptionField))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(statusLabel)
                    .addComponent(statusField))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(dueDateLabel)
                    .addComponent(dueDateField))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(addButton))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(deleteButton))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(updateButton))
                .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
                    .addComponent(viewButton))
                .addComponent(scrollPane)
        );

        // Database connection
        try {
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/todo_list", "root", "root");
            System.out.println("Connection successful!");
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Connection failed.");
        }

        // Action Listeners
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                addTask();
            }
        });

        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                deleteTask();
            }
        });

        updateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                updateTaskStatus();
            }
        });

        viewButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                viewAllTasks();
            }
        });
    }

    private void addTask() {
        String title = titleField.getText();
        String description = descriptionField.getText();
        String status = statusField.getText();
        String dueDate = dueDateField.getText();
        String currentDate = "2025-01-11"; // or get from system

        String query = "INSERT INTO tasks (title, description, status, due_date, created_at) VALUES (?, ?, ?, ?, ?)";

        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, title);
            statement.setString(2, description);
            statement.setString(3, status);
            statement.setString(4, dueDate);
            statement.setString(5, currentDate);

            statement.executeUpdate();
            JOptionPane.showMessageDialog(this, "Task added successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error adding task", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void deleteTask() {
        String taskId = JOptionPane.showInputDialog("Enter Task ID to delete:");
        int id = Integer.parseInt(taskId);

        String query = "DELETE FROM tasks WHERE id = ?";

        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, id);
            statement.executeUpdate();
            JOptionPane.showMessageDialog(this, "Task deleted successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error deleting task", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void updateTaskStatus() {
        String taskId = JOptionPane.showInputDialog("Enter Task ID to update:");
        int id = Integer.parseInt(taskId);
        String newStatus = JOptionPane.showInputDialog("Enter new Status (pending/completed):");

        String query = "UPDATE tasks SET status = ? WHERE id = ?";

        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, newStatus);
            statement.setInt(2, id);
            statement.executeUpdate();
            JOptionPane.showMessageDialog(this, "Task status updated successfully!");
        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error updating task", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void viewAllTasks() {
        String query = "SELECT * FROM tasks";

        try (Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(query)) {

            String[] columnNames = {"ID", "Title", "Description", "Status", "Due Date", "Created At"};
            DefaultTableModel model = new DefaultTableModel(columnNames, 0);

            while (resultSet.next()) {
                Object[] row = {
                    resultSet.getInt("id"),
                    resultSet.getString("title"),
                    resultSet.getString("description"),
                    resultSet.getString("status"),
                    resultSet.getDate("due_date"),
                    resultSet.getDate("created_at")
                };
                model.addRow(row);
            }

            tasksTable.setModel(model);

        } catch (SQLException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error fetching tasks", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new TodoGUI().setVisible(true);
            }
        });
    }
}
