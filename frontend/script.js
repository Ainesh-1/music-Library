document.addEventListener('DOMContentLoaded', function() {
    // Cache DOM elements
    const navItems = document.querySelectorAll('.nav-item');
    const dataTitle = document.getElementById('data-title');
    const dataContainer = document.getElementById('data-container');
    const loadingIndicator = document.getElementById('loading-indicator');
    const refreshBtn = document.getElementById('refresh-btn');
    
    // API base URL
    const API_BASE_URL = 'http://localhost:8000/';
    
    // Currently active endpoint
    let currentEndpoint = 'songs';
    
    // Initialize the page
    loadData(currentEndpoint);
    
    // Event listeners for navigation
    navItems.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Update active class
            navItems.forEach(nav => nav.classList.remove('active'));
            this.classList.add('active');
            
            // Get the endpoint from data attribute
            currentEndpoint = this.getAttribute('data-endpoint');
            
            // Update title based on endpoint
            dataTitle.textContent = capitalizeFirstLetter(currentEndpoint.split('/')[0]);
            
            // Load data for the new endpoint
            loadData(currentEndpoint);
        });
    });
    
    // Refresh button event listener
    refreshBtn.addEventListener('click', function() {
        loadData(currentEndpoint);
    });
    
    // Function to load data from API
    function loadData(endpoint) {
        // Show loading indicator
        loadingIndicator.style.display = 'block';
        dataContainer.innerHTML = '';
        
        fetch(`${API_BASE_URL}${endpoint}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                // Hide loading indicator
                loadingIndicator.style.display = 'none';
                
                // Display the data
                displayData(data, endpoint);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                loadingIndicator.style.display = 'none';
                dataContainer.innerHTML = `
                    <div class="error-message">
                        <p>Error loading data: ${error.message}</p>
                        <p>Make sure the API server is running at ${API_BASE_URL}</p>
                    </div>
                `;
            });
    }
    
    // Function to display data based on endpoint
    function displayData(data, endpoint) {
        if (!data || (Array.isArray(data) && data.length === 0)) {
            dataContainer.innerHTML = `
                <div class="empty-state">
                    <p>No data available for ${endpoint}</p>
                </div>
            `;
            return;
        }
        
        // Create a table to display the data
        const table = document.createElement('table');
        table.className = 'data-table';
        
        // Create table header
        const thead = document.createElement('thead');
        const headerRow = document.createElement('tr');
        
        // Get column names from the first item
        const firstItem = Array.isArray(data) ? data[0] : data;
        const columns = Object.keys(firstItem);
        
        // Add header cells
        columns.forEach(column => {
            const th = document.createElement('th');
            th.textContent = formatColumnName(column);
            headerRow.appendChild(th);
        });
        
        thead.appendChild(headerRow);
        table.appendChild(thead);
        
        // Create table body
        const tbody = document.createElement('tbody');
        
        // If data is an array, process each item
        if (Array.isArray(data)) {
            data.forEach(item => {
                const row = document.createElement('tr');
                
                columns.forEach(column => {
                    const cell = document.createElement('td');
                    cell.textContent = formatCellValue(item[column]);
                    row.appendChild(cell);
                });
                
                tbody.appendChild(row);
            });
        } else {
            // If data is an object, create a single row
            const row = document.createElement('tr');
            
            columns.forEach(column => {
                const cell = document.createElement('td');
                cell.textContent = formatCellValue(data[column]);
                row.appendChild(cell);
            });
            
            tbody.appendChild(row);
        }
        
        table.appendChild(tbody);
        dataContainer.appendChild(table);
    }
    
    // Helper functions
    function capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
    
    function formatColumnName(column) {
        // Convert camelCase or snake_case to Title Case
        return column
            .replace(/([A-Z])/g, ' $1') // Add space before capital letters
            .replace(/_/g, ' ')         // Replace underscores with spaces
            .replace(/^\w/, c => c.toUpperCase()); // Capitalize first letter
    }
    
    function formatCellValue(value) {
        if (value === null || value === undefined) {
            return '-';
        }
        
        if (value instanceof Date) {
            return value.toLocaleDateString();
        }
        
        if (typeof value === 'boolean') {
            return value ? 'Yes' : 'No';
        }
        
        return value.toString();
    }
});